;

var account_set_ops = {
    init:function(){
    this.enevtBind()
    },
    enevtBind:function(){
        $(".wrap_account_set .save").click(function(){
            var nickname = $(".wrap_account_set input[name=nickname]").val()
            var mobile = $(".wrap_account_set input[name=mobile]").val()
            var email = $(".wrap_account_set input[name=email]").val()
            var login_name = $(".wrap_account_set input[name=login_name]").val()
            var login_pwd = $(".wrap_account_set input[name=login_pwd]").val()
            // 校检
            if (nickname.length < 1){
                alert("昵称不符合规范")
                return false
            }
            if (mobile.length < 1){
                alert("手机号不符合规范")
                return false
            }
            if (email.length < 1){
                alert("邮箱不符合规范")
                return false
            }
            if (login_name.length < 1){
                alert("登录名不符合规范")
                return false
            }
            if (login_pwd.length < 1){
                alert("密码不符合规范")
                return false
            }

            id = $(".wrap_account_set input[name=id]").val()
            var data = {
                nickname:nickname,
                mobile:mobile,
                email:email,
                login_name:login_name,
                login_pwd:login_pwd,
                id:id
            }

            $.ajax({
                url:common_ops.buildUrl("/account/set"),
                type:"POST",
                data:data,
                dataType:"json",
                success:function(resp){
                    if (resp.code == 200){
                        window.location.href = common_ops.buildUrl("/account/index")
                    }
                    console.log(resp.msg)
                },
                error:function(error){
                    console.log(error)
                }
            })
        })
    }
}

$(document).ready(function(){
    account_set_ops.init()
})