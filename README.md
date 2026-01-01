# Real Or Render
This is a Jupyter Notebook of a neural network to differentiate AI generated images of people from images of real people.

<img width="406" height="427" alt="image" src="https://github.com/user-attachments/assets/c2d68e95-8852-4c5a-9978-f8502af9ed07" />

[This whole notebook](https://github.com/t-shimb-g/RealOrRender/blob/main/RealorRenderFinal.ipynb) was run using Google Colab's T4 GPU.

## How to Use
Since this is a Juptyer Notebook, simply run all of the scripts in order from top to bottom. I recommend utilizing Google Colab to do this.

## Examples
Below is a graph showcasing the tesing accuracy of the final model of my notebook.

<img width="680" height="659" alt="image" src="https://github.com/user-attachments/assets/b4a373d5-3d05-4f87-afe5-5613a40c293e" />

It is important to notice the training accuracy does not end up plateau-ing. This shows the model is not overfit.

The key is that both the training loss and validation loss declined in tandem. This means the model trained well enough to correctly identify new images as either `fake` or `real`.

