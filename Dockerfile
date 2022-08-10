# syntax=docker/dockerfile:1
FROM node:14-alpine
# Installing Node
# ENV NODE_VERSION=8.12.0
# RUN addgroup -g 1000 node 
# RUN adduser -u 1000 -G node -s /bin/sh -D node 
# RUN apk add --no-cache libstdc++ 
# RUN apk add --no-cache --virtual .build-deps binutils-gold curl g++ gcc gnupg libgcc linux-headers make 
# RUN /bin/sh -c for key in 94AE36675C464D64BAFA68DD7434390BDBE9B9C5 FD3A5288F042B6850C66B31F09FE44734EB7990E 71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 DD8F2338BAE7501E3DD5AC78C273792F7D83545D C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 B9AE9905FFD7803F25714661B63B535A4C206CA9 56730D5401028683275BD23C23EFEFE93C4CFFFE 77984A986EBC2AA786BC0F66B01FBB92821C587A 8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 ; do gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; done
# RUN /bin/sh -c curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz"
# RUN curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" 
# RUN gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc 
# RUN grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - 
# RUN /bin/sh -c tar -xf "node-v$NODE_VERSION.tar.xz" 
# RUN /bin/sh -c cd "node-v$NODE_VERSION" 
# RUN /bin/sh -c ./configure 
# RUN /bin/sh -c make -j$(getconf _NPROCESSORS_ONLN) 
# RUN /bin/sh -c make install 
# RUN /bin/sh -c apk del .build-deps 
# RUN /bin/sh -c cd .. 
# RUN /bin/sh -c rm -Rf "node-v$NODE_VERSION" 
# RUN rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
# Installing Yarn
# ENV YARN_VERSION=1.9.4
# RUN apk add --no-cache --virtual .build-deps-yarn curl gnupg tar 
# RUN for key in 6A010C5166006599AA17F08146C2130DFD2497F5 ; do gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; done 
# RUN curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" 
# RUN curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" 
# RUN gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz 
# RUN mkdir -p /opt 
# RUN tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ 
# RUN ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn 
# RUN ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg 
# RUN rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz 
# RUN apk del .build-deps-yarn
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add g++ make py3-setuptools py3-wheel python3-dev
RUN apk --update add libxml2-dev libxslt-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libwebp-dev libffi-dev cairo-dev pango-dev libsass
RUN pip3 install --upgrade wheel
WORKDIR /app
# COPY . .
# RUN npm install
# RUN python3 -m venv .venv
# RUN . .venv/bin/activate
# RUN pip3 install -r requirements.txt
# RUN python3 setup.py install
