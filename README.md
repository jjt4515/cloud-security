# 클라우드 보안 공격 피해자 환경
클라우드 보안 공격 자동화 플랫폼을 구현하고 테스트하기 위해 필요한 피해자 환경을 구성하였습니다.

### 주요 기능
Grafana, Loki, Prometheus, Promtail을 활용해 로그 기반 보안 공격 탐지 및 대응 

- Promtail : 로컬에서 로그 파일을 실시간으로 감시하여, 새 로그가 감지되면 Loki로 전송
- Loki : Promtail이 전송한 로그 데이터를 수집 및 저장
- Prometheus : 메트릭 데이터를 수집 및 저장
- Grafana : Loki와 Prometheus를 통해 수집한 데이터를 대시보드로 시각화
