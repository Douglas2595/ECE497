#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x99ed5c78, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0xfe990052, __VMLINUX_SYMBOL_STR(gpio_free) },
	{ 0xf20dabd8, __VMLINUX_SYMBOL_STR(free_irq) },
	{ 0x86994d78, __VMLINUX_SYMBOL_STR(gpiod_unexport) },
	{ 0x2072ee9b, __VMLINUX_SYMBOL_STR(request_threaded_irq) },
	{ 0x1b8fbaee, __VMLINUX_SYMBOL_STR(gpiod_to_irq) },
	{ 0xbcc5bb9a, __VMLINUX_SYMBOL_STR(gpiod_set_debounce) },
	{ 0xf1411218, __VMLINUX_SYMBOL_STR(gpiod_direction_input) },
	{ 0x6e3d5494, __VMLINUX_SYMBOL_STR(gpiod_export) },
	{ 0x9219e1ea, __VMLINUX_SYMBOL_STR(gpiod_direction_output_raw) },
	{ 0x47229b5c, __VMLINUX_SYMBOL_STR(gpio_request) },
	{ 0x27e1a049, __VMLINUX_SYMBOL_STR(printk) },
	{ 0xd9e4d7dc, __VMLINUX_SYMBOL_STR(gpiod_get_raw_value) },
	{ 0xd8a8c080, __VMLINUX_SYMBOL_STR(gpiod_set_raw_value) },
	{ 0x94628b6e, __VMLINUX_SYMBOL_STR(gpio_to_desc) },
	{ 0xbdfb6dbb, __VMLINUX_SYMBOL_STR(__fentry__) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "6A226B175C69A7C475DE52E");
