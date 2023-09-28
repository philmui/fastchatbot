
# Installing to AWS

```
> pip install -t dependencies -r requirements.txt
> cp templates dependencies
> (cd dependencies; zip ../aws_lambda_artifact.zip -r .)
> zip aws_lambda_artifact.zip -u server.py
```
