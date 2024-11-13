FROM public.ecr.aws/l1p7h1f9/archesproject-fargeo:7.6.x-base-dev
ENV WEB_ROOT=/web_root
ENV ARCHES_ROOT=${WEB_ROOT}/arches
ENV APP_ROOT=${WEB_ROOT}/disco
ENV NODE_MAJOR=20
ENV DEBIAN_FRONTEND=noninteractive

COPY ./arches ${ARCHES_ROOT}
RUN apt update && apt install wait-for-it openssh-client -y

COPY ../arches-for-science ${WEB_ROOT}/arches-for-science
COPY ../arches-templating ${WEB_ROOT}/arches-templating

COPY ../disco ${APP_ROOT}

RUN source ${WEB_ROOT}/ENV/bin/activate && cd ${APP_ROOT} && pip install -e '.[dev]' && \
  cd ${WEB_ROOT}/arches-for-science && pip install -e '.[dev]' && \ 
  cd ${ARCHES_ROOT} && pip install -e '.[dev]'


RUN mkdir /root/.ssh/

COPY /disco/docker/entrypoint.sh ${WEB_ROOT}/entrypoint.sh
RUN chmod -R 700 ${WEB_ROOT}/entrypoint.sh
WORKDIR ${WEB_ROOT}
ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["run_webpack"]
EXPOSE 8021
