# Board specific SELinux policy variable definitions
BOARD_SEPOLICY_DIRS += \
	vendor/samsung/common/sepolicy/BSP/bsp_marvell

BOARD_SEPOLICY_UNION += \
	adbd.te \
	asec_apk_file.te \
	atcmdsrv.te \
	at_router.te \
	bluetooth.te \
	bootanim.te \
	cache_file.te \
	codecIPC_server.te \
	core_compressor.te \
	debuggerd.te \
	device.te \
	diag.te \
	drmserver.te \
	dumpstate.te \
	eeh.te \
	env.te \
	file.te \
	file_contexts \
	FMRadiod.te \
	global_macros \
	hawk.te \
	hdcp.te \
	healthd.te \
	iml.te \
	imsc.te \
	init.te \
	installd.te \
	kernel.te \
	keystore.te \
	kmsg.te \
	lmkd.te \
	load_g_cali_data.te \
	log_on_boot.te \
	marvelltel.te \
	mediaserver.te \
	memsicd.te \
	memsicp.te \
	mned.te \
	mrvl_gpsd.te \
	mwirelessd.te \
	netd.te \
	nfc.te \
	nvm.te \
	phservice.te \
	platform_app.te \
	pppmodem.te \
	radio.te \
	recovery.te \
	rild.te \
	root_detect.te \
	run_hawk_on_boot.te \
	sdcardd.te \
	seapp_contexts \
	service_contexts \
	servicemanager.te \
	setup_fs.te \
	shell.te \
	smartcard.te \
	surfaceflinger.te \
	system_app.te \
	system_server.te \
	teecsstdca.te \
	touch_updater.te \
	ueventd.te \
	untrusted_app.te \
	vdc.te \
	vold.te \
	wpa.te \
	zygote.te