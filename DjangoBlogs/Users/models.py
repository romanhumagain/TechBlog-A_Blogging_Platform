from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from Blog.utils import generate_slugs

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    previous_logged_in_date = models.DateTimeField(null=True , blank=True)
    slug = models.SlugField(null=True,unique=True)
    profile_pic = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    bio = models.TextField(null=True, default=None)
    follower_count = models.IntegerField(null=True, default=0)
    following = models.ManyToManyField('self' , through = 'Follow' , related_name='followers' , symmetrical=False)
    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = generate_slugs(Profile, self.user.username)
            
        super().save(*args, **kwargs)  # First save the model

        image = Image.open(self.profile_pic.path)

        if image.height > 350 or image.width > 350:
            resized_size = (350, 350)
            image.thumbnail(resized_size)
            image.save(self.profile_pic.path)
            
            
class Follow(models.Model):
    follower = models.ForeignKey(Profile , related_name='following_set', on_delete=models.CASCADE)
    followed = models.ForeignKey(Profile , related_name= 'follower_ser' , on_delete=models.CASCADE)
    date_followed = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['follower' , 'followed']
        
    def __str__(self):
        return f"{self.follower.user.username} follows {self.followed.user.username}"
