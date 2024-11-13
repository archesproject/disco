FROM public.ecr.aws/l1p7h1f9/archesproject-fargeo:7.6.x-base-dev

ARG ARCHES_CORE_HOST_DIR

## Setting default environment variables
ENV WEB_ROOT=/web_root
ENV APP_ROOT=${WEB_ROOT}/disco
# Root project folder
ENV ARCHES_ROOT=${WEB_ROOT}/arches
#ENV ARCHES_TEMPLATING_ROOT=${WEB_ROOT}/arches-templating

WORKDIR ${WEB_ROOT}

# Install the Arches application
# FIXME: ADD from github repository instead?
COPY ${ARCHES_CORE_HOST_DIR} ${ARCHES_ROOT}
COPY ./arches ${ARCHES_ROOT}
RUN apt update && apt install wait-for-it openssh-client -y

COPY ../arches-for-science ${WEB_ROOT}/arches-for-science
COPY ../arches-templating ${WEB_ROOT}/arches-templating
COPY ../disco ${APP_ROOT}

RUN source ${WEB_ROOT}/ENV/bin/activate && cd ${APP_ROOT} && pip install -e '.[dev]' && \
  cd ${WEB_ROOT}/arches-for-science && pip install -e '.[dev]' && \ 
  cd ${WEB_ROOT}/arches-templating && pip install -e '.[dev]' && \ 
  cd ${ARCHES_ROOT} && pip install -e '.[dev]'

# TODO: These are required for non-dev installs, currently only depends on arches/afs
#RUN pip install -r requirements.txt

COPY /disco/docker/entrypoint.sh ${WEB_ROOT}/entrypoint.sh
RUN chmod -R 700 ${WEB_ROOT}/entrypoint.sh &&\
  dos2unix ${WEB_ROOT}/entrypoint.sh

# Set default workdir
WORKDIR ${APP_ROOT}

# # Set entrypoint
ENTRYPOINT ["../entrypoint.sh"]
CMD ["run_arches"]

# Expose port 8000
EXPOSE 8000
