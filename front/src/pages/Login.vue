<template>
    <div class="page-header clear-filter" filter-color="orange">
        <div class="page-header-image"
             style="background-image: url('img/login.jpg')">
        </div>
        <div class="content">
            <div class="container">
                <div class="col-md-5 ml-auto mr-auto">
                    <card type="login" plain>
                        <fg-input id="login"
                                  class="no-border input-lg"
                                  addon-left-icon="now-ui-icons users_circle-08"
                                  placeholder="Mail">
                        </fg-input>

                        <fg-input class="no-border input-lg"
                                  type="password"
                                  addon-left-icon="now-ui-icons text_caps-small"
                                  placeholder="Password">
                        </fg-input>

                        <template slot="raw-content">
                            <div class="card-footer text-center">
                                <a href="#pablo" class="btn btn-primary btn-round btn-lg btn-block">Connection</a>
                            </div>
                            <div class="pull-left">
                                <h6>
                                    <a href="#pablo" class="link footer-link">Create Account</a>
                                </h6>
                            </div>
                        </template>
                    </card>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { Card, Button, FormGroupInput } from '@/components';
import MainFooter from '@/layout/MainFooter';
export default {
  name: 'login-page',
  bodyClass: 'login-page',
  components: {
    Card,
    MainFooter,
    [Button.name]: Button,
    [FormGroupInput.name]: FormGroupInput
  }
};

const passwordField = document.querySelector("#password")

function switchVisibility() {
    if (passwordField.getAttribute('type') === 'password') 
        passwordField.setAttribute('type', 'text')
    else
        passwordField.setAttribute('type', 'password')
}
</script>
<style>
</style>
