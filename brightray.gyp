{
  'includes': [
    'brightray.gypi',
  ],
  'targets': [
    {
      'target_name': 'brightray',
      'type': 'static_library',
      'include_dirs': [
        '.',
        '<(libchromiumcontent_include_dir)',
        '<(libchromiumcontent_include_dir)/skia/config',
        '<(libchromiumcontent_include_dir)/third_party/skia/include/core',
        '<(libchromiumcontent_include_dir)/third_party/WebKit',
        '<(libchromiumcontent_library_dir)/gen',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '.',
          '..',
          '<(libchromiumcontent_include_dir)',
          '<(libchromiumcontent_include_dir)/skia/config',
          '<(libchromiumcontent_include_dir)/third_party/skia/include/core',
          '<(libchromiumcontent_include_dir)/third_party/icu/source/common',
          '<(libchromiumcontent_include_dir)/third_party/WebKit',
          '<(libchromiumcontent_library_dir)/gen',
        ],
      },
      'sources': [
        'browser/brightray_paths.h',
        'browser/browser_client.cc',
        'browser/browser_client.h',
        'browser/browser_context.cc',
        'browser/browser_context.h',
        'browser/browser_main_parts.cc',
        'browser/browser_main_parts.h',
        'browser/browser_main_parts_mac.mm',
        'browser/default_web_contents_delegate.cc',
        'browser/default_web_contents_delegate.h',
        'browser/default_web_contents_delegate_mac.mm',
        'browser/devtools_contents_resizing_strategy.cc',
        'browser/devtools_contents_resizing_strategy.h',
        'browser/devtools_embedder_message_dispatcher.cc',
        'browser/devtools_embedder_message_dispatcher.h',
        'browser/devtools_manager_delegate.cc',
        'browser/devtools_manager_delegate.h',
        'browser/devtools_ui.cc',
        'browser/devtools_ui.h',
        'browser/inspectable_web_contents.cc',
        'browser/inspectable_web_contents.h',
        'browser/inspectable_web_contents_delegate.cc',
        'browser/inspectable_web_contents_delegate.h',
        'browser/inspectable_web_contents_impl.cc',
        'browser/inspectable_web_contents_impl.h',
        'browser/inspectable_web_contents_view.h',
        'browser/inspectable_web_contents_view_mac.h',
        'browser/inspectable_web_contents_view_mac.mm',
        'browser/mac/bry_application.h',
        'browser/mac/bry_application.mm',
        'browser/mac/bry_inspectable_web_contents_view.h',
        'browser/mac/bry_inspectable_web_contents_view.mm',
        'browser/media/media_capture_devices_dispatcher.cc',
        'browser/media/media_capture_devices_dispatcher.h',
        'browser/media/media_stream_devices_controller.cc',
        'browser/media/media_stream_devices_controller.h',
        'browser/network_delegate.cc',
        'browser/network_delegate.h',
        'browser/notification_presenter.h',
        'browser/notification_presenter_mac.h',
        'browser/notification_presenter_mac.mm',
        'browser/platform_notification_service_impl.cc',
        'browser/platform_notification_service_impl.h',
        'browser/linux/notification_presenter_linux.h',
        'browser/linux/notification_presenter_linux.cc',
        'browser/url_request_context_getter.cc',
        'browser/url_request_context_getter.h',
        'browser/views/inspectable_web_contents_view_views.h',
        'browser/views/inspectable_web_contents_view_views.cc',
        'browser/views/views_delegate.cc',
        'browser/views/views_delegate.h',
        'browser/web_ui_controller_factory.cc',
        'browser/web_ui_controller_factory.h',
        'common/application_info.h',
        'common/application_info_mac.mm',
        'common/application_info_win.cc',
        'common/content_client.cc',
        'common/content_client.h',
        'common/mac/foundation_util.h',
        'common/mac/main_application_bundle.h',
        'common/mac/main_application_bundle.mm',
        'common/main_delegate.cc',
        'common/main_delegate.h',
        'common/main_delegate_mac.mm',
      ],
      'conditions': [
        ['libchromiumcontent_component_build', {
          'link_settings': {
            'libraries': [ '<@(libchromiumcontent_shared_libraries)' ]
          },
        }],
        ['OS=="linux"', {
          'cflags_cc': [
            '-Wno-deprecated-register',
            '-fno-rtti',
          ],
          'link_settings': {
            'ldflags': [
              '<!@(pkg-config --libs-only-L --libs-only-other gtk+-2.0 libnotify dbus-1 x11 xrandr xext gconf-2.0)',
            ],
            'libraries': [
              '<(libchromiumcontent_library_dir)/libchromiumviews.a',
              '-lpthread',
              '<!@(pkg-config --libs-only-l gtk+-2.0 libnotify dbus-1 x11 xrandr xext gconf-2.0)',
            ],
          },
        }],
        ['OS=="mac"', {
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
            ],
          },
        }],
        ['OS=="win"', {
          'link_settings': {
            'libraries': [
              '<(libchromiumcontent_library_dir)/base_static.lib',
              '<(libchromiumcontent_library_dir)/chromiumcontent.dll.lib',
              '<(libchromiumcontent_library_dir)/chromiumviews.lib',
              '<(libchromiumcontent_library_dir)/sandbox_static.lib',
            ],
          },
        }],
      ],
    },
  ],
}
