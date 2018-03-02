FROM nginx
ARG SERVER_NAME
ARG WEBAPP_PORT
ENV SERVER_NAME=$SERVER_NAME
ENV WEBAPP_PORT=$WEBAPP_PORT
ADD ./docker/proxy/nginx.conf.template /etc/nginx/nginx.conf.template
USER root
RUN envsubst '$WEBAPP_PORT $SERVER_NAME' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf