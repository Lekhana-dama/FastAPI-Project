FROM python:3.13-slim
WORKDIR /app
COPY  requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#So if your application is compromised, the attacker doesn't automatically have root privileges inside the container.
#create a non-root user (fake user)
RUN useradd -m appuser 
#giving user ownership of the application
RUN chown -R appuser:appuser /app
#switch to non-root user
USER appuser
EXPOSE 8000 
CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","8000"]