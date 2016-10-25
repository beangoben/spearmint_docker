FROM  beangoben/pimp_jupyter

USER root
#install mongo
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 &&\
    echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list


RUN apt-get update && \
    apt-get install -y mongodb-org gfortran && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /data/db &&\
    sudo chown -R $NB_USER /data/db
# Expose port 27017 from the container to the host
EXPOSE 27017

#spearmint
USER root

# Spearmint with python 3 support
#requirements
RUN conda install -c conda-forge -q -y pymongo nlopt &&\
    conda clean --all
# download source and build
RUN git clone -b python3 https://github.com/redst4r/Spearmint.git &&\
    cd Spearmint && \
    python setup.py install && \
    cd .. &&\
    rm -rf Spearmint



# Spearmint PESM
#requirements
RUN conda install -c conda-forge -n python2 -q -y pymongo pygmo=1.1.7 nlopt &&\
    conda clean --all
# download source and build
RUN source activate python2 &&\
    git clone -b PESM https://github.com/HIPS/Spearmint.git &&\
    cd Spearmint && \
    python setup.py install && \
    cd .. &&\
    rm -rf Spearmint



