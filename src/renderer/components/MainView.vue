<template>
  <div>
    <div class="main-header">- Electron Python -</div>
    <el-card :body-style="{ padding: '0px'}" style="margin: 0 20px; border-color: transparent;">
        <div slot="header">
          <span style="font-size: 18px;">Get Current Time | </span>This is an example to call RPC server API
        </div>
        <div style="padding: 20px;">
          <div style="font-size: 20px; margin-bottom: 12px;">{{currentTime}}</div>
          <div>
            <el-button type="primary" class="button" @click="getCurrentTime">GET</el-button>
          </div>
        </div>
    </el-card>
  </div>
</template>

<script>
import {manageError} from '@/utils'

export default {
  data () {
    let currentTime = 'Not Get Yet'
    return {
      currentTime
    }
  },
  methods: {
    getCurrentTime () {
      this.rpcClient.request({
        route: ':example:get-current-time'
      }).then(result => {
        this.currentTime = result
      }).catch(err => {
        manageError(this, err)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  .main-header {
    font-family: $code-font-family;
    font-size: 24px;
    text-align: center;
    padding: 24px;
    color: $--color-text-primary;
  }
</style>
