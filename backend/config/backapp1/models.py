from django.db import models
    
class AnalysisModel(models.Model):
    subreddit_name =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    post_count = models.IntegerField(default=0)
    status = models.CharField(max_length=100)
    sentiment_avg = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.subreddit_name
    
class PostAnalysedModel(models.Model):
    analysis_id = models.ForeignKey(AnalysisModel, on_delete=models.CASCADE, related_name="posts")
    reddit_id = models.CharField(max_length=50, unique=True)
    title = models.TextField()
    body = models.TextField(blank=True, default='')
    score = models.IntegerField(default=0)
    num_comments = models.IntegerField(default=0)
    created_utc = models.DateTimeField()

    def __str__(self):
        return self.analysis_id