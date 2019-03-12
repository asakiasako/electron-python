!macro preInit
 SetRegView 64
  WriteRegExpandStr HKLM "${INSTALL_REGISTRY_KEY}" InstallLocation "C:\App\Electron Python"
  WriteRegExpandStr HKCU "${INSTALL_REGISTRY_KEY}" InstallLocation "C:\App\Electron Python"
 SetRegView 32
  WriteRegExpandStr HKLM "${INSTALL_REGISTRY_KEY}" InstallLocation "C:\App\Electron Python"
  WriteRegExpandStr HKCU "${INSTALL_REGISTRY_KEY}" InstallLocation "C:\App\Electron Python"
!macroend