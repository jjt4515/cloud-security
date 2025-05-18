from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def run_security_commands():
    try:
        print("[INFO] UFW 방화벽 활성화 시도")
        subprocess.run(["sudo", "ufw", "enable"], check=False)

        print("[INFO] AppArmor 강제 실행 시도")
        subprocess.run(["sudo", "aa-enforce", "/etc/apparmor.d/"], check=False)

        print("[INFO] SELinux enforcing 모드 설정 시도")
        subprocess.run(["sudo", "setenforce", "1"], check=False)

        print("[INFO] YAMA ptrace_scope 강화 시도")
        with open("/proc/sys/kernel/yama/ptrace_scope", "w") as f:
            f.write("1")

    except Exception as e:
        print(f"[SECURITY COMMAND ERROR] {e}")

@app.route("/webhook", methods=["POST"])
def alert_handler():
    data = request.get_json()
    alerts = data.get("alerts", [])

    for alert in alerts:
        status = alert.get("status", "unknown")
        labels = alert.get("labels", {})
        annotations = alert.get("annotations", {})
        alertname = labels.get("alertname", "NoAlertName")
        instance = labels.get("instance", "NoInstance")
        summary = annotations.get("summary", "No summary provided")

        print(f"[ALERT] {alertname} on {instance} - {status}: {summary}")
        run_security_commands()

    return jsonify({"message": "Alerts processed"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
