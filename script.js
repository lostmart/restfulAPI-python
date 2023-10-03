const form = document.querySelector('form')

form.addEventListener('submit', (e) => {
	e.preventDefault()

	// Get the file input element
	const fileInput = document.getElementById('fileInput')

	const formData = new FormData(event.target)
	// Append the selected file to the FormData object
	formData.append('file', fileInput.files[0])
	fetch('http://127.0.0.1:5000/api/products', {
		method: 'POST',
		body: formData,
	}).then((response) => {
		response.json()
		console.log(response.json())
	})
})
