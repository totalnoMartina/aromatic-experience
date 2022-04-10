# Testing

## Validators of Front End


HTML5 and CSS3 documents have been validated using [Validator W3](https://validator.w3.org/)

### HTML5

Images for index and detail pages
![Index Validator](media/images/index-validated.png?raw=true)
![Detail page Validator](media/images/detail-validated.png?raw=true)

### CSS3

Image of the CSS3 validation shows an error in the '.blog' class (line 198) that specifies positioning of the blog elements which are rendered using Jinja (Django), and that includes image, date, title, author's name, likes and content of the post. The code for this styling is helping responsiveness, and works impeccable on different screen devices keeping a consistent layout and this is why I am keeping it this way. I will look more into better ways of doing this.
![CSS3 Validator](media/images/css-validation-error.png?raw=true)



