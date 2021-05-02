FROM node:14-alpine

RUN apk add --update bash 
# python3 py3-pip
# pijuice-base
# RUN pip3 install picamera 

ENV PATH="/opt/vc/bin:${PATH}"
# ADD 00-vmcs.conf /etc/ld.so.conf.d/
# RUN echo "/opt/vc/lib" > /etc/ld.so.conf.d/00-vcms.conf
# RUN ldconfig

WORKDIR /app
COPY . /app
# RUN yarn install
# RUN yarn run build
EXPOSE 3000

CMD [ "yarn", "dev" ]
#  RUN yarn install --production
#  CMD ["node", "src/index.js"]
