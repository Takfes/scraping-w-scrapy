function main(splash,args)
    splash.private_mode_enabled = fasle
    url = args.url
    assert(splash:go(url))
    assert(splash:wait(1))
    tab = assert(splash:select_all('.filterPanelItem'))
    tab[5]:mouse_click()
    assert(splash:wait(1))
    splash:set_viewport_full()
    return splash:png()
end