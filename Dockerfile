FROM  beangoben/pimp_jupyter

USER root
#install mongo
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list


RUN apt-get update && \
    apt-get install -y mongodb-org gfortran && \
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

# Spearmint with python 3 support
RUN git clone -b python3 https://github.com/redst4r/Spearmint.git &&\
    cd Spearmint && \
    python setup.py install && \
    cd .. &&\
    rm -rf Spearmint

RUN conda install -c conda-forge -q -y pymongo

#  NLOPT
RUN conda install -c conda-forge -q -y nlopt

# Spearmint PESM

RUN source activate python2 &&\
    git clone -b PESM https://github.com/HIPS/Spearmint.git &&\
    cd Spearmint && \
    python setup.py install && \
    cd .. &&\
    rm -rf Spearmint

RUN conda install -c conda-forge -n python2 -q -y pymongo

RUN conda install -c conda-forge -n python2 -q -y pygmo=1.1.7
RUN conda install -c conda-forge -n python2 -q -y nlopt



# Pygmo
#PyGMO
#USER root

#COPY docker-stuff/mongodb.service /etc/systemd/system/
#RUN sudo systemctl enable mongodb

#COPY docker-stuff/start-notebook.sh /usr/local/bin/start-notebook.sh
#RUN chmod +x /usr/local/bin/start-notebook.sh

