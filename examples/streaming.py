# load library
import hypertools as hyp

# initialize stream object
stream = hyp.Stream(port=3004, verbose=True)

hyp.plot(stream, animate='stream')
