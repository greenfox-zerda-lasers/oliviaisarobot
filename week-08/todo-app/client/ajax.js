var Ajax = function (){

	this.APIEndpoint = 'http://localhost:3000/';

	this.getTodos = function(callback) {
		this.open('GET', 'todos', false, callback);
	}

	this.newTodo = function(name, callback) {
		this.open('POST', 'new', name, callback);
	}

	this.updateTodo = function(callback) {
		this.open('PUT', 'status', false, callback);
	}

	this.deleteTodo = function(id, callback) {
		this.open('DELETE', 'remove', name, callback);
	}

	this.open = function(method, resource, data, callback) {
		var xhr = new XMLHttpRequest();
		data = (data) ? data : null;
		xhr.open( method, this.APIEndpoint + resource )

		if( method !== 'DELETE' ) {
			xhr.setRequestHeader('Content-Type', 'application/json');
		}

		xhr.send( JSON.stringify(data) );
		xhr.onreadystatechange = function (rsp) {
			if( xhr.readyState === XMLHttpRequest.DONE ) {
				callback( JSON.parse(xhr.response) );
			}
		}
	}
}
