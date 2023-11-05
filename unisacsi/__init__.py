__version__ = '0.2.24'
__authors__ = ['Lukas Frank <lukasf@unis.no', 'Jakob Dörr <jakob.dorr@uib.no']

from .Meteo import (
	read_MET_AWS,
	read_Campbell_AWS,
	read_Campbell_radiation,
    	read_miniAWS,
	read_Irgason_flux,
	read_CSAT3_flux,
	read_Tinytag,
	read_HOBO,
    	read_Raingauge,
	read_IWIN,
	read_AROME,
	read_radiosonde,
	read_iMet,
    	download_IWIN_from_THREDDS,
	initialize_empty_map,
	map_add_coastline,
	map_add_land_filled,
	map_add_bathymetry,
	map_add_total_topography,
	map_add_topography,
	map_add_surface_cover,
	map_add_crosssection_line,
	map_add_points,
	map_add_wind_arrows
)

from .Ocean import (
	cal_dist_dir_on_sphere,
	cart2pol,
	pol2cart,
	create_latlon_text,
	CTD_to_grid,
    	CTD_to_xarray,
    	section_to_xarray,
    	mooring_into_xarray,
	calc_freshwater_content,
	myloadmat,
	mat2py_time,
	present_dict,
    	ctd_identify_water_masses,
	read_ADCP_CODAS,
    	split_CODAS_resolution,
    	read_WinADCP,
    	read_LADCP,
	read_CTD,
	read_CTD_from_mat,
	read_mini_CTD,
	read_MSS,
	read_mooring_from_mat,
	read_mooring,
    	read_Seaguard,
    	read_Minilog,
    	read_SBE37,
    	read_RBR,
    	read_Thermosalinograph,
    	download_tidal_model,
	contour_section,
	plot_CTD_section,
	plot_CTD_single_section,
    	plot_xarray_sections,
	plot_CTD_station,
	plot_CTD_map,
	plot_empty_map,
	plot_CTD_ts,
	create_empty_ts,
    	check_VM_ADCP_map
)

from .MET_model_download import download_MET_model_data, download_MET_model_static_fields, MET_model_download_class
