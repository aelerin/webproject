FROM nginx:1.19.0
COPY index.html /usr/share/nginx/html
COPY favicon.ico /usr/share/nginx/html
COPY .DS_Store /usr/share/nginx/html
COPY src /usr/share/nginx/html/src
COPY assets /usr/share/nginx/html/assets
COPY fonts /usr/share/nginx/html/fonts
COPY less /usr/share/nginx/html/less
COPY css /usr/share/nginx/html/css
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
RUN apt-get update -y
EXPOSE 80
CMD ["nginx","-g","daemon off;"]