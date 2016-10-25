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

#spearmint
USER root

# Spearmint with python 3 support
#requirements
RUN conda install -c conda-forge -q -y pymongo
RUN conda install -c conda-forge -q -y nlopt
# download source and build
RUN git clone -b python3 https://github.com/redst4r/Spearmint.git &&\
    cd Spearmint && \
    python setup.py install && \
    cd .. &&\
    rm -rf Spearmint



# Spearmint PESM
#requirements
RUN conda install -c conda-forge -n python2 -q -y pymongo
RUN conda install -c conda-forge -n python2 -q -y pygmo=1.1.7
RUN conda install -c conda-forge -n python2 -q -y nlopt
# download source and build
RUN source activate python2 &&\
    git clone -b PESM https://github.com/HIPS/Spearmint.git &&\
    cd Spearmint && \
    python setup.py install && \
    cd .. &&\
    rm -rf Spearmint



