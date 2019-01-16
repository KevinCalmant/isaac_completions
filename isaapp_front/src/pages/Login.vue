<template>
    <div class="page-header clear-filter" filter-color="orange">
        <div class="page-header-image"
             style="background-image: url('img/login.jpg')">
        </div>
        <div class="content">
            <div class="container">
                <div class="col-md-5 ml-auto mr-auto">
                    <card type="login" plain>
                        <div slot="header" class="logo-container">
                            <img v-lazy="'img/now-logo.png'" alt="">
                        </div>

                        <fg-input class="no-border input-lg"
                                  placeholder="Email"
                                  v-model="form.email"
                                  addon-left-icon="now-ui-icons users_circle-08">
                        </fg-input>

                        <fg-input class="no-border input-lg"
                                  ref="password"
                                  type="password"
                                  placeholder="Password"
                                  v-model="form.password"
                                  addon-left-icon="now-ui-icons text_caps-small">
                        </fg-input>

                        <template slot="raw-content">
                            <div class="card-footer text-center">
                                 <n-button type="primary" v-on:click="connect" round block size="lg">Login</n-button>
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
import axios from 'axios';
import router from '../router';

export default {
  name: 'login-page',
  bodyClass: 'login-page',
  components: {
    Card,
    MainFooter,
    [Button.name]: Button,
    [FormGroupInput.name]: FormGroupInput
  },
  data() {
    return {
      form: {
        email: '',
        password: '',
      }
    };
   }, 
   methods: {
        connect: function() {
            const stringify = require('json-stringify-safe');

            axios.post('http://localhost:3000/api/login', {
                email: this.form.email,
                password: this.form.password
            }).then(response => {
                // this.$store.commit('LOGIN_SUCCESS', response);
                router.push("/")
            }).catch(error => {
                console.error(stringify(error));
                console.log(stringify(error))
            });
        }
    }
};
</script>
<style>
</style>
