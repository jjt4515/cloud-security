# Java 17이 설치된 공식 이미지를 기반으로 함 (버전 필요시 수정)
FROM openjdk:17-jdk-alpine

# JAR 파일을 컨테이너 내부로 복사할 건데,
# 이 경로는 빌드 결과물 경로를 기준으로 맞춰줘야 함
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} /app.jar

# 컨테이너 시작 시 JAR 실행
ENTRYPOINT ["java", "-jar", "/app.jar"]
