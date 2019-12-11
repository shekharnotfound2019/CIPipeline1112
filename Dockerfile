FROM ubuntu:16.04
LABEL MAINTAINER shekhar@gmail.com
RUN mkdir /code
RUN echo "Image is built ..."
COPY sample.sh /code/sample.sh
RUN chmod +x /code/sample.sh
ENTRYPOINT ["sh","/code/sample.sh"]
CMD [ "/etc/hosts"]
