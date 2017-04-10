'''This script demonstrates how to build a variational autoencoder with Keras.

Reference: "Auto-Encoding Variational Bayes" https://arxiv.org/abs/1312.6114
'''
import numpy as np
from keras.layers import Input, Dense, Lambda
from keras.models import Model
from keras import backend as K
from keras import metrics
from keras.datasets import mnist
import json


def read_params(json_file):
    params = json.loads(open(json_file).read())
    return params


def main():
    p = read_params("params.json")
    print('Using parameters:')
    for key, value in p.items():
        print('{:20s} - {:12}'.format(key, value))

    intermediate_dim = int(2**p['intermediate_dim'])
    latent_dim = int(p['latent_dim'])
    dec_h_activation = p['dec_h_activation']
    dec_mean_activation = p['dec_mean_activation']

    batch_size = 100
    original_dim = 784
    epochs = 25
    epsilon_std = 1.0

    def vae_loss(x, x_decoded_mean):
        xent_loss = original_dim * \
            metrics.binary_crossentropy(x, x_decoded_mean)
        kl_loss = - 0.5 * K.sum(1 + z_log_var -
                                K.square(z_mean) - K.exp(z_log_var), axis=-1)
        return xent_loss + kl_loss

    def sampling(args):
        z_mean, z_log_var = args
        epsilon = K.random_normal(shape=(batch_size, latent_dim), mean=0.,
                                  stddev=epsilon_std)
        return z_mean + K.exp(z_log_var / 2) * epsilon

    x = Input(batch_shape=(batch_size, original_dim))
    h = Dense(intermediate_dim, activation=dec_h_activation)(x)
    z_mean = Dense(latent_dim)(h)
    z_log_var = Dense(latent_dim)(h)

    # note that "output_shape" isn't necessary with the TensorFlow backend
    z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])

    # we instantiate these layers separately so as to reuse them later
    decoder_h = Dense(intermediate_dim, activation=dec_h_activation)
    decoder_mean = Dense(original_dim, activation=dec_mean_activation)
    h_decoded = decoder_h(z)
    x_decoded_mean = decoder_mean(h_decoded)

    vae = Model(x, x_decoded_mean)
    vae.compile(optimizer='rmsprop', loss=vae_loss)

    # train the VAE on MNIST digits
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

    hist = vae.fit(x_train, x_train,
                   shuffle=True,
                   epochs=epochs,
                   batch_size=batch_size,
                   validation_data=(x_test, x_test))

    result = hist.history['loss'][-1]
    print(' Final Result = {}'.format(result))
    print('**FINISHED**')
    return

if __name__ == "__main__":
    main()
