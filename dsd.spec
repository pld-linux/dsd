Summary:	Digital Speech Decoder
Name:		dsd
Version:	1.6.0
Release:	1
License:	BSD
Group:		Applications/Engineering
Source0:	https://github.com/szechyjs/dsd/archive/v%{version}.tar.gz
# Source0-md5:	e1c8faf8b0156215ffefee6a614e07a3
URL:		https://github.com/szechyjs/dsd
BuildRequires:	mbelib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DSD is able to decode several digital voice formats from discriminator
tap audio and synthesize the decoded speech.

Supported formats:
- P25 Phase 1
- ProVoice
- X2-TDMA
- DMR/MOTOTRBO
- NXDN
- D-STAR

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install dsd $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/dsd
