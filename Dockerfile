FROM  beangoben/pimp_jupyter

USER root
#install mongo
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list


RUN apt-get update && \
    apt-get install -y mongodb-org cmake && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data/db
# Expose port 27017 from the container to the host
EXPOSE 27017
# Set usr/bin/mongod as the dockerized entry-point application
RUN sudo chown -R $NB_USER /data/db

RUN conda install -c anaconda boost

#spearmint
USER root

#RUN git clone -b PESC https://github.com/HIPS/Spearmint.git &&\
#spearmint with python 3 support
RUN git clone -b python3 https://github.com/redst4r/Spearmint.git
#COPY Spearmint3/ /home/$NB_USER/work/Spearmint3
RUN mv Spearmint Spearmint3 && \
    cd Spearmint3 && \
    python setup.py install && \
    rm -rf .git
    #cd .. &&\
    #rm -rf Spearmint
RUN pip install pymongo

#  NLOPT

#RUN wget http://ab-initio.mit.edu/nlopt/nlopt-2.4.2.tar.gz
#RUN tar -zxvf nlopt-2.4.2.tar.gz
#RUN cd nlopt-2.4.2 &&\
#    mkdir build &&\
#    ./configure --enable-shared &&\
#    make &&\
#    make install

# Pygmo
#PyGMO
#USER root

#COPY docker-stuff/mongodb.service /etc/systemd/system/
#RUN sudo systemctl enable mongodb

#COPY docker-stuff/start-notebook.sh /usr/local/bin/start-notebook.sh
#RUN chmod +x /usr/local/bin/start-notebook.sh

