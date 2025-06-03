



Inference time compute is a hot topic in 2025 - how can we improve the performance of LLMs and agentic workflows through better prompting, fine-tuning on thinking datasets, or unique search approaches?

Working on a image classification problem, after training a model, I attempted classification. It performed fairly well (98% accuracy), but there were still some errors. How do I do better? I could go back and test more architectures, search out some new datasets, do some ensembling of the models I trained. Many good options. But what if I just thought about it a bit longer? When the model is uncertain (as it is in most of my failure cases), can it think a bit more to arrive at better results? With a typical CNN, not particularly. You could try augmenting the input example in various ways and average across the predictions (that's certainly what I do with live examples when the results aren't quite correct), but the mileage is limited.

Instead, could we perform some search at inference time? 

If the dataset has some underlying logic / structure, then our classifier should be finding the most 'logical' example. For example, for the problem of MNIST, we have Spatial Transformer Networks (STNs) which transform an image (in a gradient friendly way) to a standard representation before running classification. While the transformation is still a neural network parameterised by weights, by first transforming the image to what seems most reasonable we're suggesting the model should classify given some underlying structure, minimising the cross entropy between the generating process and the model.




e.g. searching latent space for image classification

Why don't we do test time search for image classification? CNNs are so fast but that's not a requirement for many tasks!!


Methods:
 - MC Inference and Bayesian Estimation (e.g. 30 forward passes gives Bayesian effect)
 - Test time augmentation: apply transforms at test time, run inference for each view [tried running an experiment for this, but didn't yield good results]
 - recurrent refinement: Recurrent Convolutional Network (RCN), ConvGRU, create hidden states for T turns then predict. ; predict-refine loop
 - gradient based test-time adaptation
 - score maximisation over latent programs: search over combination of transformations that yields a high-confidence digit class (need to account for the fact that it could just squish everything to be yi (1), priors, train the priors into a neural network, neural guided search)

