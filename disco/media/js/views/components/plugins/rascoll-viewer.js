define([
    'knockout',
    'templates/views/components/plugins/rascoll-viewer.htm'
], function(ko, RascollViewerTemplate) {

    var EmbedViewer = function(params) {
        var self = this;
    };

    return ko.components.register('rascoll-viewer', {
        viewModel: EmbedViewer,
        template: RascollViewerTemplate
    });
});
