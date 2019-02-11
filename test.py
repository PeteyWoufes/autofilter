import autofilter.google_api, autofilter.create_label, autofilter.create_filter, autofilter.group_manager


def main():
    autofilter.create_label.main(autofilter.google_api)
    autofilter.create_filter.main(autofilter.google_api)
    autofilter.group_manager.main(autofilter.google_api)

if __name__ == "__main__":
    main()