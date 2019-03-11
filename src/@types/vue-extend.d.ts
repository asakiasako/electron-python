import Vue from 'vue'
import { AllElectron } from 'electron'

declare module 'vue/types/vue' {
  interface Vue {
    $electron: AllElectron
    bus: Vue
    appState: object
    rpcClient: {
      invoke(
        apiCategory: string, 
        apiName: string, 
        ...args: any[]
      ): void,
      invokes(
        apiCategory: string,
        apiName: string,
        ...args: any[]
      ): Promise<any>,
      disconnectServer(address: string): void,
      connectServer(address: string): void,
      request(params: object): any
    }
  }
}