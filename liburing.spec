Name: liburing
Version: 0.3
Release: 1%{?dist}
Summary: Linux-native io_uring I/O access library
License: LGPLv2+
Source: https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz
URL: https://git.kernel.dk/cgit/liburing/
BuildRequires: gcc

# Fails to build and therefore isn't supported upstream
ExcludeArch: armv7hl

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package devel
Summary: Development files for Linux-native io_uring I/O access library
Requires: %{name}%{_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%prep
%autosetup

%build
%set_build_flags
./configure --prefix=%{_prefix} --libdir=/%{_libdir} --mandir=%{_mandir} --includedir=%{_includedir}

%make_build

%install
%make_install

%files
%attr(0755,root,root) %{_libdir}/liburing.so.*
%license COPYING

%files devel
%{_includedir}/liburing/
%{_includedir}/liburing.h
%{_libdir}/liburing.so
%exclude %{_libdir}/liburing.a
%{_libdir}/pkgconfig/*
%{_mandir}/man2/*

%changelog
* Tue Jan 7 2020 Stefan Hajnoczi <stefanha@redhat.com> - 0.3-1
- Add IORING_OP_STATX
- Add IORING_OP_OPENAT/IORING_OP_CLOSE helpers
- Add prep helpers for IORING_OP_FILES_UPDATE and IORING_OP_FALLOCATE
- Add io_uring_prep_connect() helper
- Add io_uring_wait_cqe_nr()
- Add IORING_OP_ASYNC_CANCEL and prep helper

* Thu Oct 31 2019 Jeff Moyer <jmoyer@redhat.com> - 0.2-1
- Add io_uring_cq_ready()
- Add io_uring_peek_batch_cqe()
- Add io_uring_prep_accept()
- Add io_uring_prep_{recv,send}msg()
- Add io_uring_prep_timeout_remove()
- Add io_uring_queue_init_params()
- Add io_uring_register_files_update()
- Add io_uring_sq_space_left()
- Add io_uring_wait_cqe_timeout()
- Add io_uring_wait_cqes()
- Add io_uring_wait_cqes_timeout()

* Tue Jan 8 2019 Jens Axboe <axboe@kernel.dk> - 0.1
- Initial version