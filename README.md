
# A URL shortener but instead of shortening the URL it makes it look extremely dodgy

### Sample URLs:
```
twitter.com -> win.a.free.ipad.verylegit.link/CT*OMGb=B5+b+)u6)DU882bitcoin.xlsx.pdf
google.com -> paypal.verylegit.link/8U70*m[uO409index.apk.pem.dmg
verylegit.link -> click.here.to.get.ripped.in.three.weeks.verylegit.link/ip-camera()698download!downloader.min.css.dmg
```

### How does it work?
When you give it a URL, a randomy sketchy URL path (the bit after the /) is generated. The mapping between the real URL and the sketchy one is then saved.
Since only the part after the / matters, you can use any domain you like.

#### Example

All of these links go to the same place (this page):
```
verylegit.link/exploit+411botnet.xlsx.rar.pdf
win2003.verylegit.link/exploit+411botnet.xlsx.rar.pdf
<anything>.verylegit.link/exploit+411botnet.xlsx.rar.pdf
```

## API
```
POST /sketchify
{
    'long_url': 'twitter.com'
}
```
Will return
```
   win.a.free.ipad.verylegit.link/CT*OMGb=B5+b+)u6)DU882bitcoin.xlsx.pdf

```

Go for it!

## Questions?
@ me on twitter: [@mangopdf](https://twitter.com/mangopdf)

This whole thing was inspired by wanting to give [ShadyURL](http://shadyurl.com) some new and spicy features.

