 浏览器默认的样式就是这样的，默认情况下<body>的宽度就比<html>小的，原因是<body>和<html>的内外边框所导致。因此我们在与CSS样式表的时候都要进行“reset”：

* {
  outline: 0;
  padding: 0;
  margin: 0;
  border: 0;
}
消除了默认的内外边框之后，<body>的宽度就与<html>相同了。
box-sizing 属性可以被用来调整这些表现:

content-box  
是默认值。如果你设置一个元素的宽为100px，那么这个元素的内容区会有100px 宽，
并且任何边框和内边距的宽度都会被增加到最后绘制出来的元素宽度中。
border-box 
告诉浏览器去理解你设置的边框和内边距的值是包含在width内的。也就是说，
如果你将一个元素的width设为100px,那么这100px会包含其它的border和padding，
内容区的实际宽度会是width减去border + padding的计算值。大多数情况下这使得我们
更容易的去设定一个元素的宽高。
