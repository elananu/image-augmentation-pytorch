
!pip install torch torchvision pillow matplotlib -q

import PIL.Image
import matplotlib.pyplot as plt
from torchvision import transforms

def imshow(img_path, transform, title):

img_path = "sample_image.jpg"

fig, ax = plt.subplots(1, 2, figsize=(15, 4))

ax[0].set_title('Original')
ax[0].imshow(img)
ax[0].axis('off')

transformed_img = transform(img)
ax[1].set_title(title)
ax[1].imshow(transformed_img)
ax[1].axis('off')

save_path = f"/content/{title.replace(' ', '_').lower()}.png"
transformed_img.save(save_path)
print(f" Saved: {save_path}")
plt.show()

img_path = "/content/2cc24bc422ba9c48236b13ac0aca1145.jpg"

loader_transform = transforms.Resize((140, 140))
imshow(img_path, loader_transform, 'Scaling')

loader_transform = transforms.CenterCrop(140)
imshow(img_path, loader_transform, 'Center Crop')

loader_transform = transforms.RandomHorizontalFlip(p=1)
imshow(img_path, loader_transform, 'Horizontal Flip')

loader_transform = transforms.Pad((2, 5, 0, 5))
imshow(img_path, loader_transform, 'Padding')

loader_transform = transforms.RandomRotation(30)
imshow(img_path, loader_transform, 'Rotation')

loader_transform = transforms.RandomAffine(0, translate=(0.4, 0.5))
imshow(img_path, loader_transform, 'Affine Transformation')

img = PIL.Image.open(img_path)
fig, ax = plt.subplots(2, 2, figsize=(16, 10))

loader_transform1 = transforms.ColorJitter(brightness=2)
img1 = loader_transform1(img)
ax[0, 0].set_title('Brightness')
ax[0, 0].imshow(img1)
ax[0, 0].axis('off')
img1.save('/content/brightness.png')

loader_transform2 = transforms.ColorJitter(contrast=2)
img2 = loader_transform2(img)
ax[0, 1].set_title('Contrast')
ax[0, 1].imshow(img2)
ax[0, 1].axis('off')
img2.save('/content/contrast.png')

img3 = loader_transform3(img)
ax[1, 0].set_title('Saturation')
ax[1, 0].imshow(img3)
ax[1, 0].axis('off')
img3.save('/content/saturation.png')

loader_transform4 = transforms.ColorJitter(hue=0.2)
img4 = loader_transform4(img)
ax[1, 1].set_title('Hue')
ax[1, 1].imshow(img4)
ax[1, 1].axis('off')
img4.save('/content/hue.png')
fig.savefig('/content/color_augmentation.png', bbox_inches='tight')
print("Saved: /content/color_augmentation.png")
plt.show()

loader_transform = transforms.Grayscale()
imshow(img_path, loader_transform, 'Grayscale')

loader_transform = transforms.Compose([
transforms.RandomRotation(30),
transforms.RandomResizedCrop(140),
transforms.RandomHorizontalFlip()

])
imshow(img_path, loader_transform, 'Combined Transformations')
