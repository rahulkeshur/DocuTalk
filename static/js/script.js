const pdfFile = document.getElementById('pdfFile');
const fileName = document.getElementById('fileName');

pdfFile.addEventListener('change', function () {

  if(this.files.length > 0){
    fileName.textContent = 'Selected File: ' + this.files[0].name;
  }
  else{
    fileName.textContent = 'No file selected';
  }

});

function submitData(){

  const file = pdfFile.files[0];
  const question = document.getElementById('question').value;

  if(!file || question.trim() === ''){
    alert('Please upload PDF and enter your question');
    return;
  }

  alert('PDF Uploaded Successfully!');

}

// Flask backend API here
