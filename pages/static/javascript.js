(function(win,doc){
    'use strict';

    //Ajax do form
    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form');
        function sendForm(event)
        {
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN',token);
            ajax.onreadystatechange = function()
            {
                if(ajax.status === 200 && ajax.readyState === 4){
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Operação realizada com sucesso!';
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                }
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit',sendForm,false);
    }
})(window,document);

/*
$("#form").validate({
    rules : {
        id_payment_id:{
                    required:true,
                    minlength:1
        },
        id_start_date:{
                required:true,
                minlength:1
        },
        id_end_date:{
                required:true,
                minlength:1
        },
        id_original_value:{
                required:true,
                minlength:1
        },
        id_collaborator_owner:{
                required:true,
                minlength:1
        },
        id_social_bussiness_name:{
                required:true,
                minlength:1
        },
        id_CNPJ:{
                required:true,
                minlength:1
        }                                
    },
    messages:{
        id_payment_id:{
                    required:"Por favor, informe seu nome",
                    minlength:"O nome deve ter pelo menos 3 caracteres"
        },
        id_start_date:{
                required:"A mensagem não pode ficar em branco"
        },
        id_end_date:{
                required:"A mensagem não pode ficar em branco"
        },     
        id_original_value:{
                required:"A mensagem não pode ficar em branco"
        },     
        id_collaborator_owner:{
                required:"A mensagem não pode ficar em branco"
        },     
        id_social_bussiness_name:{
                required:"A mensagem não pode ficar em branco"
        },     
        id_CNPJ:{
                required:"A mensagem não pode ficar em branco",
                minlength:"O CNPJ informado deve conter 14 caracteres"
        }       
    }
}); */



