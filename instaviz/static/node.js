
//three types of objects
//	array
//  object
//  function

var transforms = {
	'object':{'tag':'div','class':'package ${show} ${type}','children':[
		{'tag':'div','class':'header','children':[
			{'tag':'div','class':function(obj){

				var classes = ["arrow"];

				if( getValue(obj.value) !== undefined ) classes.push("hide");

				return(classes.join(' '));
			}},
			{'tag':'span','class':'name','html':'${name}'},
			{'tag':'span','class':'value','html':function(obj) {
				var value = getValue(obj.value);
				if( value !== undefined ) return(" : " + value);
				else return('');
			}},
			{'tag':'span','class':'type','html':'${type}'}
		]},
		{'tag':'div','class':'children','children':function(obj){return(children(obj.value));}}
	]}
};

function visualize(json) {

	$('#selection').html('');

	$('#selection').json2html(convert('json',json,'open'),transforms.object);

	regEvents();
}

function getValue(obj) {
	var type = $.type(obj);

	//Determine if this object has children
	switch(type) {
		case 'array':
		case 'object':
			return(undefined);
		break;

		case 'function':
			//none
			return('function');
		break;

		case 'string':
			return("'" + obj + "'");
		break;

		default:
			return(obj);
		break;
	}
}

//Transform the children
function children(obj){
	var type = $.type(obj);

	//Determine if this object has children
	switch(type) {
		case 'array':
		case 'object':
			return(json2html.transform(obj,transforms.object));
		break;

		default:
			//This must be a literal
		break;
	}
}

function convert(name,obj,show) {

	var type = $.type(obj);

	if(show === undefined) show = 'open';

	var children = [];

	//Determine the type of this object
	switch(type) {
		case 'array':
			//Transform array
			//Itterrate through the array and add it to the elements array
			var len=obj.length;
			for(var j=0;j<len;++j){
				//Concat the return elements from this objects tranformation
				children[j] = convert(j,obj[j]);
			}
		break;

		case 'object':
			//Transform Object
			var j = 0;
			for(var prop in obj) {
				children[j] = convert(prop,obj[prop]);
				j++;
			}
		break;

		default:
			//This must be a litteral (or function)
			children = obj;
		break;
	}

	return( {'name':name,'value':children,'type':type,'show':show} );

}

function regEvents() {
	$('.header').click(function(){
		var parent = $(this).parent();

		if(parent.hasClass('closed')) {
			parent.removeClass('closed');
			parent.addClass('open');
		} else {
			parent.removeClass('open');
			parent.addClass('closed');
		}
	});
}
