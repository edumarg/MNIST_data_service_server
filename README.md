"# MNIST_data_service_server"
Server to get a specific amount of training images from the MNIST database. The images and labels are store in the
server and where obtain from http://yann.lecun.com/exdb/mnist/

The client should send a GET request to the following path </images?quantity=" and add the number of requested images
for example to get only 3 images then "/images?quantity=3". The default quantity is 10.

