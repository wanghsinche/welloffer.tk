// loading a zip file
var mypg = document.querySelector('progress');
JSZipUtils.onprogress = function(total,current){
	mypg.max = total;
	mypg.value = current;
};

JSZipUtils.getBinaryContent('./big.zip', function (err, data) {
   if(err) {
      throw err; // or handle the error
   }
   var zipFile = new JSZip();
   JSZip.loadAsync(data)
	.then(function(zipContent) {
		return Promise.all(Object.keys(zipContent.files).sort().map(function(filename){
			return zipContent.file(filename).async("base64");
		}));
	})
	.then(function(resls){
		var imgls = resls.map(function(v){
			var img = new Image();
			img.src = 'data:image/png;base64,'+v;
			document.body.appendChild(img);
		});
	});
});