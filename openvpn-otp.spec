Summary:	OpenVPN HOTP/TOTP plugin
Summary(pl.UTF-8):	Wtyczka HOTP/TOTP dla OpenVPN
Name:		openvpn-otp
Version:	1.0
Release:	1
License:	GPL v3
Group:		Networking/Daemons
Source0:	https://github.com/evgeny-gridasov/openvpn-otp/archive/v%{version}.tar.gz
# Source0-md5:	3ff2b8f9cc054ccac31f99e9ee704f67
Patch1:		https://github.com/evgeny-gridasov/openvpn-otp/commit/2d3809abca1909a3a8a55fa8e38d5c139faf3d59.patch
# Patch1-md5:	b199454e79e9c9cb962cbde9626429a0
URL:		https://github.com/evgeny-gridasov/openvpn-otp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	openvpn-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/%{_lib}/openvpn/plugins
%define		_sysconfdir	/etc/openvpn

%description
Support for time based OTP and HMAC based OTP tokens for OpenVPN.
Compatible with Google Authenticator software token, other software
and hardware based OTP tokens.

%description -l pl.UTF-8
Wtyczka implementuje uwierzytelnianie hasłami jednorazowymi.

%prep
%setup -q
%patch -P1 -p1

%build
%{__mkdir_p} m4
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-openvpn-plugin-dir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/openvpn-otp.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/%{name}.so
