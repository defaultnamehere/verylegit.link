
# A URL shortener but instead of shortening the URL it makes it look extremely dodgy

### Sample URLs:
```
twitter.com -> http://verylegit.link/movie_119windows-updat.html.min.js.pdf
google.com -> very.verylegit.link/825pcspeedup.xlsx.zip
verylegit.link -> definitely.verylegit.link/torrent_718windows7$speedupurpc.msi.gif.zip
http://www.reactiongifs.com/wp-content/uploads/2013/02/firefly.gif -> http://not.verylegit.link/79password_.dmg.rar
```

### How does it work?
When you give it a URL, a randomy sketchy URL path (the bit after the /) is generated. The mapping between the real URL and the sketchy one is then saved.
Since only the part after the / matters, you can use any domain you like.

#### Example

All of these links go to the same place (this page):
```
verylegit.link/970free-iphone(.gif.docm.sh
not.verylegit.link/970free-iphone(.gif.docm.sh
novelty.website/970free-iphone(.gif.docm.sh
sketchify-42ef3.appspot-preview.com//970free-iphone(.gif.docm.sh
<whatever_you_want>.verylegit.link/970free-iphone(.gif.docm.sh
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
http://verylegit.link/movie_119windows-updat.html.min.js.pdf
```

Go for it!

## Questions?
@ me on twitter: [@_notlikethis](https://twitter.com/_notlikethis)
This whole thing was inspired by wanting to give [ShadyURL](http://shadyurl.com) some new and spicy features.

