FROM openjdk:17
WORKDIR /app
COPY . .
EXPOSE 25565
CMD ["java", "-Xmx1024M", "-Xms1024M", "-jar", "server.jar", "nogui"]
